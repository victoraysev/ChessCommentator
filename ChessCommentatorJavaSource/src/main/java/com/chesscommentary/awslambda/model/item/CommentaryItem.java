package com.chesscommentary.awslambda.model.item;

import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBAttribute;
import com.chesscommentary.awslambda.model.Comment;

public class CommentaryItem {

    private Comment comment;

    @DynamoDBAttribute(attributeName = "M")
    public Comment getCommentary() {
        return comment;
    }

    public void setCommentary(Comment comment) {
        this.comment = comment;
    }
}
