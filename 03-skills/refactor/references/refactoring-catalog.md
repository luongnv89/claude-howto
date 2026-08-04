# Refactoring Catalog

A curated catalog of refactoring techniques from Martin Fowler's *Refactoring* (2nd Edition). Each refactoring includes motivation, step-by-step mechanics, and examples.

> "A refactoring is defined by its mechanics—the precise sequence of steps that you follow to carry out the change." — Martin Fowler

---

## How to Use This Catalog

1. **Identify the smell** using the code smells reference
2. **Find the matching refactoring** in this catalog
3. **Follow the mechanics** step by step
4. **Test after each step** to ensure behavior is preserved

**Golden Rule**: If any step takes more than 10 minutes, break it into smaller steps.

---

## Most Common Refactorings

### Extract Method

**When to use**: Long method, duplicate code, need to name a concept

**Motivation**: Turn a code fragment into a method whose name explains the purpose.

**Mechanics**:
1. Create a new method named for what it does (not how)
2. Copy the code fragment into the new method
3. Scan for local variables used in the fragment
4. Pass local variables as parameters (or declare in method)
5. Handle return values appropriately
6. Replace the original fragment with a call to the new method
7. Test

**Before**:
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // Calculate outstanding
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // Print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**After**:
```javascript
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

---

### Inline Method

**When to use**: Method body is as clear as its name, excessive delegation

**Motivation**: Remove needless indirection when the method doesn't add value.

**Mechanics**:
1. Check that the method isn't polymorphic
2. Find all calls to the method
3. Replace each call with the method body
4. Test after each replacement
5. Remove the method definition

**Before**:
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**After**:
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### Extract Variable

**When to use**: Complex expression that is hard to understand

**Motivation**: Give a name to a piece of a complex expression.

**Mechanics**:
1. Ensure the expression has no side effects
2. Declare an immutable variable
3. Set it to the result of the expression (or part)
4. Replace the original expression with the variable
5. Test

**Before**:
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**After**:
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### Inline Variable

**When to use**: Variable name doesn't communicate more than the expression

**Motivation**: Remove unnecessary indirection.

**Mechanics**:
1. Check that the right-hand side has no side effects
2. If variable isn't immutable, make it so and test
3. Find the first reference and replace with the expression
4. Test
5. Repeat for all references
6. Remove the declaration and assignment
7. Test

---

### Rename Variable

**When to use**: Name doesn't clearly communicate purpose

**Motivation**: Good names are crucial for clean code.

**Mechanics**:
1. If variable is widely used, consider encapsulating
2. Find all references
3. Change each reference
4. Test

**Tips**:
- Use intention-revealing names
- Avoid abbreviations
- Use domain terminology

```javascript
// Bad
const d = 30;
const x = users.filter(u => u.a);

// Good
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### Change Function Declaration

**When to use**: Function name doesn't explain purpose, parameters need change

**Motivation**: Good function names make code self-documenting.

**Mechanics (Simple)**:
1. Remove parameters not needed
2. Change the name
3. Add parameters needed
4. Test

**Mechanics (Migration - for complex changes)**:
1. If removing parameter, make sure it's not used
2. Create new function with desired declaration
3. Have old function call new function
4. Test
5. Change callers to use new function
6. Test after each
7. Remove old function

**Before**:
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**After**:
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### Encapsulate Variable

**When to use**: Direct access to data from multiple places

**Motivation**: Provide a clear access point for data manipulation.

**Mechanics**:
1. Create getter and setter functions
2. Find all references
3. Replace reads with getter
4. Replace writes with setter
5. Test after each change
6. Restrict visibility of the variable

**Before**:
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// Used in many places
spaceship.owner = defaultOwner;
```

**After**:
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### Introduce Parameter Object

**When to use**: Several parameters that frequently go together

**Motivation**: Group data that naturally belongs together.

**Mechanics**:
1. Create a new class/structure for the grouped parameters
2. Test
3. Use Change Function Declaration to add the new object
4. Test
5. For each parameter in the group, remove it from the function and use the new object
6. Test after each

**Before**:
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**After**:
```javascript
class DateRange {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }
}

function amountInvoiced(dateRange) { ... }
function amountReceived(dateRange) { ... }
function amountOverdue(dateRange) { ... }
```

---

### Combine Functions into Class

**When to use**: Several functions operate on the same data

**Motivation**: Group functions with the data they operate on.

**Mechanics**:
1. Apply Encapsulate Record to the common data
2. Move each function into the class
3. Test after each move
4. Replace data arguments with uses of class fields

**Before**:
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**After**:
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### Split Phase

**When to use**: Code deals with two different things

**Motivation**: Separate code into distinct phases with clear boundaries.

**Mechanics**:
1. Create a second function for the second phase
2. Test
3. Introduce an intermediate data structure between phases
4. Test
5. Extract first phase into its own function
6. Test

**Before**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  const shippingPerCase = (basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = quantity * shippingPerCase;
  return basePrice - discount + shippingCost;
}
```

**After**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const priceData = calculatePricingData(product, quantity);
  return applyShipping(priceData, shippingMethod);
}

function calculatePricingData(product, quantity) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  return { basePrice, quantity, discount };
}

function applyShipping(priceData, shippingMethod) {
  const shippingPerCase = (priceData.basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = priceData.quantity * shippingPerCase;
  return priceData.basePrice - priceData.discount + shippingCost;
}
```

---

## Moving Features

### Move Method

**When to use**: Method uses more features of another class than its own

**Motivation**: Put functions with the data they use most.

**Mechanics**:
1. Examine all program elements used by method in its class
2. Check if method is polymorphic
3. Copy method to target class
4. Adjust for new context
5. Make original method delegate to target
6. Test
7. Consider removing original method

---

### Move Field

**When to use**: Field is used more by another class

**Motivation**: Keep data with the functions that use it.

**Mechanics**:
1. Encapsulate the field if not already
2. Test
3. Create field in target
4. Update references to use target field
5. Test
6. Remove original field

---

### Move Statements into Function

**When to use**: Same code always appears with a function call

**Motivation**: Remove duplication by moving repeated code into the function.

**Mechanics**:
1. Extract the repeated code into a function if not already
2. Move statements into that function
3. Test
4. If callers no longer need standalone statements, remove them

---

### Move Statements to Callers

**When to use**: Common behavior varies between callers

**Motivation**: When behavior needs to differ, move it out of the function.

**Mechanics**:
1. Use Extract Method on the code to move
2. Use Inline Method on the original function
3. Remove the now-inlined call
4. Move extracted code to each caller
5. Test

---

## Organizing Data

### Replace Primitive with Object

**When to use**: Data item needs more behavior than simple value

**Motivation**: Encapsulate data with its behavior.

**Mechanics**:
1. Apply Encapsulate Variable
2. Create a simple value class
3. Change the setter to create a new instance
4. Change the getter to return the value
5. Test
6. Add richer behavior to the new class

**Before**:
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // string: "high", "rush", etc.
  }
}

// Usage
if (order.priority === "high" || order.priority === "rush") { ... }
```

**After**:
```javascript
class Priority {
  constructor(value) {
    if (!Priority.legalValues().includes(value))
      throw new Error(`Invalid priority: ${value}`);
    this._value = value;
  }

  static legalValues() { return ['low', 'normal', 'high', 'rush']; }
  get value() { return this._value; }

  higherThan(other) {
    return Priority.legalValues().indexOf(this._value) >
           Priority.legalValues().indexOf(other._value);
  }
}

// Usage
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### Replace Temp with Query

**When to use**: Temporary variable holds result of an expression

**Motivation**: Make the code clearer by extracting the expression into a function.

**Mechanics**:
1. Check that the variable is assigned only once
2. Extract the assignment's right-hand side into a method
3. Replace references to the temp with the method call
4. Test
5. Remove the temp declaration and assignment

**Before**:
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**After**:
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// In the method
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## Simplifying Conditional Logic

### Decompose Conditional

**When to use**: Complex conditional (if-then-else) statement

**Motivation**: Make the intention clear by extracting conditions and actions.

**Mechanics**:
1. Apply Extract Method on the condition
2. Apply Extract Method on the then-branch
3. Apply Extract Method on the else-branch (if present)

**Before**:
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**After**:
```javascript
if (isSummer(aDate, plan)) {
  charge = summerCharge(quantity, plan);
} else {
  charge = regularCharge(quantity, plan);
}

function isSummer(date, plan) {
  return !date.isBefore(plan.summerStart) && !date.isAfter(plan.summerEnd);
}

function summerCharge(quantity, plan) {
  return quantity * plan.summerRate;
}

function regularCharge(quantity, plan) {
  return quantity * plan.regularRate + plan.regularServiceCharge;
}
```

---

### Consolidate Conditional Expression

**When to use**: Multiple conditions with the same result

**Motivation**: Make it clear that conditions are a single check.

**Mechanics**:
1. Verify no side effects in conditions
2. Combine conditions using `and` or `or`
3. Consider Extract Method on the combined condition

**Before**:
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**After**:
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### Replace Nested Conditional with Guard Clauses

**When to use**: Deeply nested conditionals making flow hard to follow

**Motivation**: Use guard clauses for special cases, keeping normal flow clear.

**Mechanics**:
1. Find the special case conditions
2. Replace them with guard clauses that return early
3. Test after each change

**Before**:
```javascript
function payAmount(employee) {
  let result;
  if (employee.isSeparated) {
    result = { amount: 0, reasonCode: "SEP" };
  } else {
    if (employee.isRetired) {
      result = { amount: 0, reasonCode: "RET" };
    } else {
      result = calculateNormalPay(employee);
    }
  }
  return result;
}
```

**After**:
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### Replace Conditional with Polymorphism

**When to use**: Switch/case based on type, conditional logic varying by type

**Motivation**: Let objects handle their own behavior.

**Mechanics**:
1. Create class hierarchy (if not exists)
2. Use Factory Function for object creation
3. Move conditional logic into superclass method
4. Create subclass method for each case
5. Remove original conditional

**Before**:
```javascript
function plumages(birds) {
  return birds.map(b => plumage(b));
}

function plumage(bird) {
  switch (bird.type) {
    case 'EuropeanSwallow':
      return "average";
    case 'AfricanSwallow':
      return (bird.numberOfCoconuts > 2) ? "tired" : "average";
    case 'NorwegianBlueParrot':
      return (bird.voltage > 100) ? "scorched" : "beautiful";
    default:
      return "unknown";
  }
}
```

**After**:
```javascript
class Bird {
  get plumage() { return "unknown"; }
}

class EuropeanSwallow extends Bird {
  get plumage() { return "average"; }
}

class AfricanSwallow extends Bird {
  get plumage() {
    return (this.numberOfCoconuts > 2) ? "tired" : "average";
  }
}

class NorwegianBlueParrot extends Bird {
  get plumage() {
    return (this.voltage > 100) ? "scorched" : "beautiful";
  }
}

function createBird(data) {
  switch (data.type) {
    case 'EuropeanSwallow': return new EuropeanSwallow(data);
    case 'AfricanSwallow': return new AfricanSwallow(data);
    case 'NorwegianBlueParrot': return new NorwegianBlueParrot(data);
    default: return new Bird(data);
  }
}
```

---

### Introduce Special Case (Null Object)

**When to use**: Repeated null checks for special cases

**Motivation**: Return a special object that handles the special case.

**Mechanics**:
1. Create special case class with expected interface
2. Add isSpecialCase check
3. Introduce factory method
4. Replace null checks with special case object usage
5. Test

**Before**:
```javascript
const customer = site.customer;
// ... many places checking
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**After**:
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// Factory method
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// Usage - no null checks needed
const customerName = customer.name;
```

---

## Refactoring APIs

### Separate Query from Modifier

**When to use**: Function both returns a value and has side effects

**Motivation**: Make it clear which operations have side effects.

**Mechanics**:
1. Create a new query function
2. Copy original function's return logic
3. Modify original to return void
4. Replace calls that use return value
5. Test

**Before**:
```javascript
function alertForMiscreant(people) {
  for (const p of people) {
    if (p === "Don") {
      setOffAlarms();
      return "Don";
    }
    if (p === "John") {
      setOffAlarms();
      return "John";
    }
  }
  return "";
}
```

**After**:
```javascript
function findMiscreant(people) {
  for (const p of people) {
    if (p === "Don") return "Don";
    if (p === "John") return "John";
  }
  return "";
}

function alertForMiscreant(people) {
  if (findMiscreant(people) !== "") setOffAlarms();
}
```

---

### Parameterize Function

**When to use**: Several functions doing similar things with different values

**Motivation**: Remove duplication by adding a parameter.

**Mechanics**:
1. Select one function
2. Add parameter for the varying literal
3. Change body to use the parameter
4. Test
5. Change callers to use the parameterized version
6. Remove now-unused functions

**Before**:
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**After**:
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// Usage
raise(person, 0.10);
raise(person, 0.05);
```

---

### Remove Flag Argument

**When to use**: Boolean parameter that changes function behavior

**Motivation**: Make the behavior explicit through separate functions.

**Mechanics**:
1. Create explicit function for each flag value
2. Replace each call with appropriate new function
3. Test after each change
4. Remove original function

**Before**:
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // premium booking logic
  } else {
    // regular booking logic
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**After**:
```javascript
function bookPremiumConcert(customer) {
  // premium booking logic
}

function bookRegularConcert(customer) {
  // regular booking logic
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## Dealing with Inheritance

### Pull Up Method

**When to use**: Same method in multiple subclasses

**Motivation**: Remove duplication in class hierarchy.

**Mechanics**:
1. Inspect methods to ensure they are identical
2. Check signatures are the same
3. Create new method in superclass
4. Copy body from one subclass
5. Delete one subclass method, test
6. Delete other subclass methods, test each

---

### Push Down Method

**When to use**: Behavior relevant only to a subset of subclasses

**Motivation**: Put method where it's used.

**Mechanics**:
1. Copy method to each subclass that needs it
2. Remove method from superclass
3. Test
4. Remove from subclasses that don't need it
5. Test

---

### Replace Subclass with Delegate

**When to use**: Inheritance is being used incorrectly, need more flexibility

**Motivation**: Prefer composition over inheritance when appropriate.

**Mechanics**:
1. Create empty class for delegate
2. Add field to host class holding delegate
3. Create constructor for delegate, called from host
4. Move features to delegate
5. Test after each move
6. Replace inheritance with delegation

---

## Extract Class

**When to use**: Large class with multiple responsibilities

**Motivation**: Split class to maintain single responsibility.

**Mechanics**:
1. Decide how to split responsibilities
2. Create new class
3. Move field from original to new class
4. Test
5. Move methods from original to new class
6. Test after each move
7. Review and rename both classes
8. Decide how to expose new class

**Before**:
```javascript
class Person {
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get officeAreaCode() { return this._officeAreaCode; }
  set officeAreaCode(arg) { this._officeAreaCode = arg; }
  get officeNumber() { return this._officeNumber; }
  set officeNumber(arg) { this._officeNumber = arg; }

  get telephoneNumber() {
    return `(${this._officeAreaCode}) ${this._officeNumber}`;
  }
}
```

**After**:
```javascript
class Person {
  constructor() {
    this._telephoneNumber = new TelephoneNumber();
  }
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get telephoneNumber() { return this._telephoneNumber.toString(); }
  get officeAreaCode() { return this._telephoneNumber.areaCode; }
  set officeAreaCode(arg) { this._telephoneNumber.areaCode = arg; }
}

class TelephoneNumber {
  get areaCode() { return this._areaCode; }
  set areaCode(arg) { this._areaCode = arg; }
  get number() { return this._number; }
  set number(arg) { this._number = arg; }
  toString() { return `(${this._areaCode}) ${this._number}`; }
}
```

---

## Quick Reference: Smell to Refactoring

| Code Smell | Primary Refactoring | Alternative |
|------------|-------------------|-------------|
| Long Method | Extract Method | Replace Temp with Query |
| Duplicate Code | Extract Method | Pull Up Method |
| Large Class | Extract Class | Extract Subclass |
| Long Parameter List | Introduce Parameter Object | Preserve Whole Object |
| Feature Envy | Move Method | Extract Method + Move |
| Data Clumps | Extract Class | Introduce Parameter Object |
| Primitive Obsession | Replace Primitive with Object | Replace Type Code |
| Switch Statements | Replace Conditional with Polymorphism | Replace Type Code |
| Temporary Field | Extract Class | Introduce Null Object |
| Message Chains | Hide Delegate | Extract Method |
| Middle Man | Remove Middle Man | Inline Method |
| Divergent Change | Extract Class | Split Phase |
| Shotgun Surgery | Move Method | Inline Class |
| Dead Code | Remove Dead Code | - |
| Speculative Generality | Collapse Hierarchy | Inline Class |

---

## Further Reading

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Online catalog: https://refactoring.com/catalog/

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
