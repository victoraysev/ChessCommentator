package com.chesscommentary.awslambda.model.converter;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBTypeConverter;
import com.chesscommentary.awslambda.model.Comment;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.util.Map;

public class CommentaryMapConverter implements DynamoDBTypeConverter<String, Map<String, Comment>> {

    private static final ObjectMapper objectMapper = new ObjectMapper();

    @Override
    public String convert(Map<String, Comment> commentaries) {
        if (commentaries == null || commentaries.isEmpty()) {
            return null;
        }

        try {
            return objectMapper.writeValueAsString(commentaries);
        } catch (JsonProcessingException e) {
            throw new IllegalArgumentException("Error converting Map to JSON", e);
        }
    }

    @Override
    public Map<String, Comment> unconvert(String json) {
        if (json == null || json.isEmpty()) {
            return null;
        }

        try {
            return objectMapper.readValue(json, new TypeReference<Map<String, Comment>>() {});
        } catch (IOException e) {
            throw new IllegalArgumentException("Error converting JSON to Map", e);
        }
    }
}
