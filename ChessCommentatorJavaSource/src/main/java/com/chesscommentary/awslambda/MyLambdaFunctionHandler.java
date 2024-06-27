package com.chesscommentary.awslambda;

import com.chesscommentary.awslambda.apigateway.APIGatewayRequest;
import org.springframework.cloud.function.adapter.aws.SpringBootRequestHandler;

import java.util.List;

public class MyLambdaFunctionHandler extends SpringBootRequestHandler<APIGatewayRequest, List<Object>> {
}
