package com.example.porquin.controller;

import com.example.porquin.dao.Categoria;
import com.example.porquin.repository.CategoriaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CategoriaController {

    @Autowired
    CategoriaRepository categoriaRepository;

    @PostMapping("/cadastrar-categoria")
    public ResponseEntity<Categoria> cadastrarCategoria(@RequestBody Categoria categoria){

        Categoria categoriaSalva = categoriaRepository.save(categoria);
        if(categoriaSalva == null){
            return ResponseEntity.status(500).body(categoriaSalva);
        }

        return ResponseEntity.ok().body(categoriaSalva);
    }

}
