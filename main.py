import requests
import os
import dotenv
from mcp.server.fastmcp import FastMCP

dotenv.load_dotenv()

mcp = FastMCP(name="Yonote MCP Server")
API_TOKEN = os.getenv("API_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL") or "https://app.yonote.ru/api"

@mcp.tool(
    name="documents_list",
    description="Get list of documents"
)
def documents_list(limit: int = 0, offset: int = 0, collectionId: str = ""):
    headers = {
        'authorization': f'Bearer {API_TOKEN}',
        'content-type': 'application/json',
        'accept': 'application/json'
    }
    body = {}
    if limit > 0:
        body["limit"] = limit
    if offset > 0:
        body["offset"] = offset
    if collectionId:
        body["collectionId"] = collectionId
    try:
        response = requests.post(
            f"{API_BASE_URL}/documents.list",
            headers=headers,
            json=body
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Exception when calling documents.list: {e}")
        raise e

@mcp.tool(
    name="documents_info",
    description="Get info about a document by id"
)
def documents_info(id: str):
    headers = {
        'authorization': f'Bearer {API_TOKEN}',
        'content-type': 'application/json',
        'accept': 'application/json'
    }
    try:
        response = requests.post(
            f"{API_BASE_URL}/documents.info",
            headers=headers,
            json={"id": id}  # Pass the id as required by the API
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Exception when calling documents.info: {e}")
        raise e

@mcp.tool(
    name="collections_list",
    description="Get list of collections"
)
def collections_list(limit: int = 0, offset: int = 0):
    headers = {
        'authorization': f'Bearer {API_TOKEN}',
        'content-type': 'application/json',
        'accept': 'application/json'
    }
    body = {}
    if limit > 0:
        body["limit"] = limit
    if offset > 0:
        body["offset"] = offset
    try:
        response = requests.post(
            f"{API_BASE_URL}/collections.list",
            headers=headers,
            json=body
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Exception when calling collections.list: {e}")
        raise e

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
