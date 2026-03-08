from fastmcp import FastMCP
import os

mcp = FastMCP("file-tools")


@mcp.tool()
def list_files(path: str = "."):
    """List files in a directory"""
    try:
        return os.listdir(path)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def read_file(path: str):
    """Read file contents"""
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    mcp.run()
