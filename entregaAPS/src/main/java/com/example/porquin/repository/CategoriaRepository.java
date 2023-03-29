package com.example.porquin.repository;

import com.example.porquin.dao.Categoria;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface CategoriaRepository extends JpaRepository<Categoria, Long> {

    Categoria save(Categoria categoria);
}
