package com.chesscommentary.awslambda.apigateway;

public class APIGatewayRequest {

    private String httpMethod;

    public String getHttpMethod() {
        return httpMethod;
    }

    public void setHttpMethod(String httpMethod) {
        this.httpMethod = httpMethod;
    }

}
