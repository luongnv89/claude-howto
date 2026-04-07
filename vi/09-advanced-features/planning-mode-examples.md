# Planning Mode Examples

Real-world examples demonstrating effective use of planning mode in Claude Code.

## Example 1: Building a REST API

### Without Planning Mode

```
User: Build a REST API for a blog

Claude: I'll create the API...
[Starts coding immediately, may miss requirements]
```

### With Planning Mode

```
User: /plan Build a REST API for a blog

Claude: Let me create a comprehensive plan for the blog API.

## Blog REST API Implementation Plan

### Phase 1: Project Setup (15 min)
1. Initialize Node.js project with Express
2. Set up TypeScript configuration
3. Install dependencies (express, pg, jwt, joi)
4. Configure environment variables
5. Set up project structure

### Phase 2: Database Layer (30 min)
6. Design database schema
   - users table (id, email, password_hash, created_at)
   - posts table (id, user_id, title, content, published, created_at, updated_at)
   - comments table (id, post_id, user_id, content, created_at)
7. Create migration files
8. Set up database connection pool
9. Implement database models

### Phase 3: Authentication (45 min)
10. Implement user registration endpoint
11. Implement login endpoint with JWT
12. Create authentication middleware
13. Add password hashing with bcrypt
14. Implement token refresh logic

### Phase 4: Posts API (40 min)
15. GET /api/posts - List all published posts (with pagination)
16. GET /api/posts/:id - Get single post
17. POST /api/posts - Create new post (auth required)
18. PUT /api/posts/:id - Update post (auth required, ownership check)
19. DELETE /api/posts/:id - Delete post (auth required, ownership check)
20. GET /api/users/:id/posts - Get user's posts

### Phase 5: Comments API (30 min)
21. GET /api/posts/:id/comments - Get post comments
22. POST /api/posts/:id/comments - Add comment (auth required)
23. DELETE /api/comments/:id - Delete comment (auth required, ownership check)

### Phase 6: Validation & Error Handling (30 min)
24. Add request validation with Joi
25. Implement global error handler
26. Add input sanitization
27. Implement rate limiting

### Phase 7: Testing (60 min)
28. Write unit tests for models
29. Write integration tests for auth endpoints
30. Write integration tests for posts endpoints
31. Write integration tests for comments endpoints
32. Achieve 80%+ code coverage

### Phase 8: Documentation & Deployment (30 min)
33. Generate API documentation with Swagger
34. Create README with setup instructions
35. Add Docker configuration
36. Set up CI/CD pipeline

**Estimated Time**: 4.5 hours
**Files to Create**: ~25
**Key Technologies**: Express, PostgreSQL, JWT, TypeScript

**API Endpoints Summary**:
- Authentication: 2 endpoints
- Posts: 6 endpoints
- Comments: 3 endpoints
- Total: 11 endpoints

Ready to proceed? (yes/no/modify)

User: yes

Claude: Starting Phase 1: Project Setup...
[Implements each phase systematically]
```

## Example 2: Database Migration

### With Planning Mode

```
User: /plan Migrate from MongoDB to PostgreSQL

Claude: This is a complex migration. Let me create a detailed plan.

## MongoDB to PostgreSQL Migration Plan

### Phase 1: Analysis & Preparation (Day 1)
1. Analyze current MongoDB schema
2. Identify data relationships and constraints
3. Document current data volume and growth rate
4. Design equivalent PostgreSQL schema
5. Plan data type mappings
6. Identify potential migration challenges

### Phase 2: PostgreSQL Setup (Day 1)
7. Set up PostgreSQL database
8. Create schema with tables, indexes, constraints
9. Set up connection pooling
10. Configure backup strategy

### Phase 3: Dual-Write Implementation (Day 2-3)
11. Create database abstraction layer
12. Implement dual-write to both databases
13. Add data consistency checks
14. Deploy dual-write to staging
15. Monitor for issues

### Phase 4: Data Migration (Day 4)
16. Create data export scripts for MongoDB
17. Create data import scripts for PostgreSQL
18. Implement data transformation logic
19. Run initial migration on copy of production data
20. Validate migrated data integrity

### Phase 5: Gradual Cutover (Day 5-7)
21. Enable dual-write in production
22. Migrate historical data in batches
23. Continuously validate data consistency
24. Monitor both databases
25. Fix any data synchronization issues

### Phase 6: PostgreSQL Primary (Day 8)
26. Switch read operations to PostgreSQL
27. Monitor query performance
28. Optimize slow queries
29. Continue dual-write for safety

### Phase 7: MongoDB Retirement (Day 9-10)
30. Stop writing to MongoDB
31. Keep MongoDB as backup for 2 weeks
32. Remove MongoDB dependencies from code
33. Archive MongoDB data
34. Decommission MongoDB instance

**Estimated Time**: 10 days
**Risk Level**: High
**Rollback Strategy**: Keep MongoDB running with dual-write
**Success Criteria**:
- Zero data loss
- <5% performance regression
- All tests passing

**Key Risks**:
1. Data inconsistency during migration
2. Query performance degradation
3. Application downtime
4. Data loss

**Mitigation**:
- Dual-write pattern for safety
- Gradual cutover
- Continuous monitoring
- Quick rollback capability

Proceed with this plan? (yes/no/modify)

User: Modify - let's add a rollback plan for each phase

Claude: Updated plan with rollback procedures for each phase...
```

## Example 3: Frontend Refactoring

```
User: /plan Refactor our React app from class components to hooks

Claude: I'll create a systematic refactoring plan.

## React Class to Hooks Migration Plan

### Phase 1: Preparation & Analysis (2 hours)
1. Audit all class components (find all .jsx/.tsx files)
2. Categorize by complexity:
   - Simple (state only): ~15 components
   - Medium (lifecycle methods): ~23 components
   - Complex (multiple lifecycle, refs): ~8 components
3. Identify third-party libraries that need updates
4. Create component dependency graph
5. Plan migration order (leaf nodes first)

### Phase 2: Setup & Tooling (1 hour)
6. Update React to v18+
7. Set up ESLint rules for hooks
8. Create conversion templates
9. Set up automated tests
10. Create checkpoint before starting

### Phase 3: Migrate Simple Components (4 hours)
11. Convert simple stateful components (15 components)
12. Replace this.state with useState
13. Replace this.setState with state setters
14. Test each component after conversion
15. Update tests

### Phase 4: Migrate Medium Components (8 hours)
16. Convert components with lifecycle methods (23 components)
17. Replace componentDidMount with useEffect
18. Replace componentDidUpdate with useEffect
19. Replace componentWillUnmount with useEffect cleanup
20. Test thoroughly

### Phase 5: Migrate Complex Components (12 hours)
21. Convert complex components (8 components)
22. Replace refs with useRef
23. Extract custom hooks for shared logic
24. Handle edge cases (multiple useEffect)
25. Extensive testing

### Phase 6: Shared Logic Extraction (6 hours)
26. Identify duplicated logic across components
27. Create custom hooks:
    - useAuth
    - useFetch
    - useLocalStorage
    - useDebounce
28. Refactor components to use custom hooks
29. Test custom hooks independently

### Phase 7: Performance Optimization (4 hours)
30. Add React.memo where needed
31. Optimize with useCallback
32. Optimize with useMemo
33. Profile and fix performance regressions

### Phase 8: Cleanup & Documentation (2 hours)
34. Remove unused class component utilities
35. Update documentation
36. Update coding guidelines
37. Create migration guide for team

**Estimated Time**: 5 days (39 hours)
**Files to Modify**: 46 components
**Risk Level**: Medium

**Migration Order**:
1. Leaf components (no dependencies)
2. Mid-level components
3. Top-level container components
4. App.jsx (last)

**Testing Strategy**:
- Unit tests for each component
- Integration tests for user flows
- Visual regression tests
- Performance benchmarks

**Success Metrics**:
- All tests passing
- No visual regressions
- Performance maintained or improved
- Bundle size not significantly increased

Proceed? (yes/no/modify)
```

## Example 4: Security Implementation

```
User: /plan Implement comprehensive security for our web app

Claude: Let me create a thorough security implementation plan.

## Web Application Security Implementation Plan

### Phase 1: Security Audit (Day 1)
1. Run automated security scanners (npm audit, Snyk)
2. Review dependencies for vulnerabilities
3. Check OWASP Top 10 compliance
4. Audit authentication flows
5. Review data handling practices
6. Document current security gaps

### Phase 2: Authentication Hardening (Day 2-3)
7. Implement strong password requirements
8. Add password strength meter
9. Implement rate limiting on login
10. Add account lockout after failed attempts
11. Implement 2FA (TOTP)
12. Add session management improvements
13. Implement secure password reset flow

### Phase 3: Authorization & Access Control (Day 3-4)
14. Implement RBAC (Role-Based Access Control)
15. Add permission checks on all endpoints
16. Implement principle of least privilege
17. Add audit logging for sensitive operations
18. Implement resource-level permissions

### Phase 4: Data Protection (Day 4-5)
19. Implement encryption at rest (sensitive fields)
20. Ensure TLS/SSL for all communications
21. Implement secure session storage
22. Add PII data masking in logs
23. Implement data retention policies
24. Add secure file upload handling

### Phase 5: Input Validation & Sanitization (Day 5-6)
25. Implement input validation on all endpoints
26. Add XSS protection (Content Security Policy)
27. Implement SQL injection prevention (parameterized queries)
28. Add CSRF protection
29. Implement request size limits
30. Add file upload type validation

### Phase 6: Security Headers & Configuration (Day 6)
31. Add security headers:
    - Strict-Transport-Security
    - X-Content-Type-Options
    - X-Frame-Options
    - X-XSS-Protection
    - Content-Security-Policy
32. Configure CORS properly
33. Disable unnecessary HTTP methods
34. Remove server version headers

### Phase 7: Monitoring & Logging (Day 7)
35. Implement security event logging
36. Add anomaly detection
37. Set up intrusion detection
38. Implement real-time alerting
39. Create security dashboard

### Phase 8: Testing & Documentation (Day 8-9)
40. Perform penetration testing
41. Run security scanners
42. Test all security features
43. Create security documentation
44. Train team on security practices
45. Create incident response plan

### Phase 9: Compliance & Policies (Day 10)
46. GDPR compliance check
47. Create privacy policy
48. Implement data subject rights
49. Add cookie consent
50. Create security policies documentation

**Estimated Time**: 10 days
**Risk Level**: Critical
**Priority**: High

**Security Improvements Summary**:
- Authentication: 7 enhancements
- Authorization: 5 enhancements
- Data Protection: 6 enhancements
- Input Validation: 6 enhancements
- Infrastructure: 9 enhancements
- Monitoring: 5 enhancements

**Compliance**: OWASP Top 10, GDPR

**Success Criteria**:
- Zero critical vulnerabilities
- All OWASP Top 10 mitigated
- Security score >90/100
- All pen test issues resolved

Proceed? (yes/no/modify)
```

## Example 5: Performance Optimization

```
User: /plan Optimize our slow e-commerce website

Claude: Let me create a comprehensive performance optimization plan.

## E-commerce Performance Optimization Plan

### Phase 1: Performance Audit (4 hours)
1. Run Lighthouse audit
2. Analyze Chrome DevTools performance profile
3. Measure Core Web Vitals:
   - LCP (Largest Contentful Paint)
   - FID (First Input Delay)
   - CLS (Cumulative Layout Shift)
4. Identify performance bottlenecks
5. Create baseline performance metrics

**Current Metrics**:
- LCP: 4.2s (target: <2.5s)
- FID: 280ms (target: <100ms)
- CLS: 0.25 (target: <0.1)
- Page Load: 8.3s (target: <3s)

### Phase 2: Image Optimization (6 hours)
6. Convert images to WebP format
7. Implement responsive images
8. Add lazy loading for images
9. Optimize image sizes (compression)
10. Implement CDN for images
11. Add image placeholders

**Expected Impact**: -40% load time

### Phase 3: Code Splitting & Lazy Loading (8 hours)
12. Implement route-based code splitting
13. Lazy load non-critical components
14. Split vendor bundles
15. Optimize chunk sizes
16. Implement dynamic imports
17. Add preloading for critical resources

**Expected Impact**: -30% initial bundle size

### Phase 4: Caching Strategy (6 hours)
18. Implement browser caching (Cache-Control)
19. Add service worker for offline support
20. Implement API response caching
21. Add Redis cache for database queries
22. Implement stale-while-revalidate
23. Configure CDN caching

**Expected Impact**: -50% API response time

### Phase 5: Database Optimization (8 hours)
24. Add database indexes
25. Optimize slow queries (>100ms)
26. Implement query result caching
27. Add connection pooling
28. Denormalize where appropriate
29. Implement database read replicas

**Expected Impact**: -60% database query time

### Phase 6: Frontend Optimization (10 hours)
30. Minimize and compress JavaScript
31. Minimize and compress CSS
32. Remove unused CSS (PurgeCSS)
33. Implement critical CSS
34. Defer non-critical JavaScript
35. Reduce DOM size
36. Optimize React rendering (memo, useMemo)
37. Implement virtual scrolling for long lists

**Expected Impact**: -35% JavaScript execution time

### Phase 7: Network Optimization (4 hours)
38. Enable HTTP/2
39. Implement resource hints (preconnect, prefetch)
40. Reduce number of HTTP requests
41. Enable Brotli compression
42. Optimize third-party scripts

**Expected Impact**: -25% network time

### Phase 8: Monitoring & Testing (4 hours)
43. Set up performance monitoring (Datadog/New Relic)
44. Add Real User Monitoring (RUM)
45. Create performance budgets
46. Set up automated Lighthouse CI
47. Test on real devices

**Estimated Time**: 50 hours (2 weeks)

**Target Metrics** (90th percentile):
- LCP: <2.0s (from 4.2s) ✅
- FID: <50ms (from 280ms) ✅
- CLS: <0.05 (from 0.25) ✅
- Page Load: <2.5s (from 8.3s) ✅

**Expected Revenue Impact**:
- 100ms faster = 1% conversion increase
- Target: 5.8s improvement = ~58% conversion increase
- Estimated additional revenue: Significant

**Priority Order**:
1. Image optimization (quick wins)
2. Code splitting (high impact)
3. Caching (high impact)
4. Database optimization (critical)
5. Frontend optimization (polish)

Proceed with this plan? (yes/no/modify)
```

## Key Takeaways

### Benefits of Planning Mode

1. **Clarity**: Clear roadmap before starting
2. **Estimation**: Time and effort estimates
3. **Risk Assessment**: Identify potential issues early
4. **Prioritization**: Logical order of tasks
5. **Approval**: Review and approve before execution
6. **Modification**: Adjust plan based on feedback

### When to Use Planning Mode

✅ **Always use for**:
- Multi-day projects
- Team collaborations
- Critical system changes
- Learning new concepts
- Complex refactoring

❌ **Don't use for**:
- Bug fixes
- Small tweaks
- Simple queries
- Quick experiments

### Best Practices

1. **Review plans carefully** before approving
2. **Modify plans** when you spot issues
3. **Break down** complex tasks
4. **Estimate realistic** timeframes
5. **Include rollback** strategies
6. **Add success** criteria
7. **Plan for testing** at each phase
