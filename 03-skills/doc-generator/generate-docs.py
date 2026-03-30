#!/usr/bin/env python3
import ast
import os
import sys


class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
        if node.name.startswith("get_") or node.name.startswith("post_"):
            doc = ast.get_docstring(node)
            endpoint = {
                "name": node.name,
                "docstring": doc,
                "params": [arg.arg for arg in node.args.args],
                "returns": self._extract_return_type(node),
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"


def generate_markdown_docs(endpoints: list[dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs


def _validate_input_path(raw_path: str) -> str:
    """Validate and sanitize a file path to prevent path traversal attacks.

    Resolves the real absolute path, ensures it remains within the current
    working directory, and restricts input to Python source files only.

    Args:
        raw_path: The raw file path supplied by the user.

    Returns:
        The validated, resolved absolute path.

    Raises:
        SystemExit: If the path fails any validation check.
    """
    real_path = os.path.realpath(raw_path)
    allowed_base = os.path.realpath(os.getcwd())

    # Ensure the resolved path stays inside the allowed base directory
    if not (real_path == allowed_base or real_path.startswith(allowed_base + os.sep)):
        print(
            "Error: Access to files outside the current directory is not allowed.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Only process Python source files
    if not real_path.endswith(".py"):
        print("Error: Only Python (.py) files are supported.", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(real_path):
        print(f"Error: File not found: {real_path}", file=sys.stderr)
        sys.exit(1)

    return real_path


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate API documentation from a Python source file."
    )
    parser.add_argument("source_file", help="Path to the Python source file to document")
    args = parser.parse_args()

    # Validate and sanitize the input path before any file I/O
    safe_path = _validate_input_path(args.source_file)

    with open(safe_path) as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
