package com.chesscommentary.awslambda.model;

import java.util.List;
import java.util.Map;

import com.amazonaws.services.dynamodbv2.datamodeling.*;

@DynamoDBTable(tableName = "Game")
public class Game {
    @DynamoDBHashKey(attributeName = "id") // id will be your hash key attribute
    private String id;
    @DynamoDBAttribute(attributeName = "commentaries")
    private List<Comment> commentaries;
    private List<String> hashtags;
    private String pgn;
    private Map<String, String> players;

    // Getters and Setters
    // You can generate these using your IDE or manually define them

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Comment> getCommentaries() {
        return commentaries;
    }

    public void setCommentaries(List<Comment> commentaries) {
        this.commentaries = commentaries;
    }

    public List<String> getHashtags() {
        return hashtags;
    }

    public void setHashtags(List<String> hashtags) {
        this.hashtags = hashtags;
    }

    public String getPgn() {
        return pgn;
    }

    public void setPgn(String pgn) {
        this.pgn = pgn;
    }

    public Map<String, String> getPlayers() {
        return players;
    }

    public void setPlayers(Map<String, String> players) {
        this.players = players;
    }
}
