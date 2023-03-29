package com.example.porquin.services;

import com.example.porquin.dao.Categoria;
import com.example.porquin.repository.CategoriaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

@Service
@Scope("singleton")
public class CategoriaService {
    @Autowired
    CategoriaRepository categoriaRepository;

    public Categoria cadastrarCategoria(Categoria categoria){
        return categoriaRepository.save(categoria);
    }
}
