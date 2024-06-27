package com.chesscommentary.awslambda.functions;

import com.chesscommentary.awslambda.apigateway.APIGatewayResponse;
import com.chesscommentary.awslambda.model.Game;
import com.chesscommentary.awslambda.repository.GameRepository;
import com.chesscommentary.awslambda.apigateway.APIGatewayRequest;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.*;
import java.util.function.Function;

@Component
public class GetGamesFunction implements Function<APIGatewayRequest, APIGatewayResponse> {

    @Autowired
    private GameRepository gameRepository;

    @Override
    public APIGatewayResponse  apply(APIGatewayRequest userRequest) {
        List<Game> games = new ArrayList<>();
        try {
            Iterator<Game> itr = gameRepository.findAll().iterator();
            while (itr.hasNext()) {
                games.add(itr.next());
            }
            // Convert the list of games to JSON
            ObjectMapper objectMapper = new ObjectMapper();
            String body = objectMapper.writeValueAsString(games);

            // Create the response
            Map<String, String> headers = new HashMap<>();
            headers.put("Content-Type", "application/json");

            return new APIGatewayResponse(200, headers, body);
        } catch (Exception e) {
            System.err.println("Error retrieving games: " + e.getMessage());
            e.printStackTrace();

            // Error response
            Map<String, String> headers = new HashMap<>();
            headers.put("Content-Type", "application/json");

            return new APIGatewayResponse(500, headers, "{\"message\": \"Internal Server Error\"}");
        }    }
}
