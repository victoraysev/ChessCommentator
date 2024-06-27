package com.chesscommentary.awslambda.repository;

import com.chesscommentary.awslambda.model.Game;
import org.socialsignin.spring.data.dynamodb.repository.EnableScan;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface GameRepository extends CrudRepository<Game, String> {

    @EnableScan
    Iterable<Game> findAll();
}
