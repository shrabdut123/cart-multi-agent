def generate_openapi_spec(tools):
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "MCP Server API",
            "version": "1.0.0",
            "description": "OpenAPI spec auto-generated from MCP tools."
        },
        "paths": {}
    }

    for tool in tools:
        path = f"/{tool.name}"
        spec["paths"][path] = {
            "post": {
                "summary": tool.description,
                "operationId": tool.name,
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": tool.inputSchema
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {
                            "application/json": {
                                "schema": tool.outputSchema
                            }
                        }
                    }
                }
            }
        }
    return spec