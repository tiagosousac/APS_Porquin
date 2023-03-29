package com.example.porquin.controller;

import com.example.porquin.dao.Gasto;
import com.example.porquin.repository.GastoRepository;
import com.example.porquin.services.Facade;
import com.example.porquin.services.GastoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController()
public class GastoController {

    @Autowired
    Facade facade;
    @PostMapping("/cadastrar-gasto")
    public ResponseEntity<Gasto> cadastrarGasto(@RequestBody Gasto gastoRequest) {
        Gasto gastoSalve = facade.cadastrarGasto(gastoRequest);
        if(gastoSalve == null){
            return ResponseEntity.status(500).body(gastoSalve);
        }

        return ResponseEntity.ok().body(gastoSalve);
    }

    @PostMapping("/cadastrar-gastos")
    public ResponseEntity<List<Gasto>> cadastrarGastos(@RequestBody List<Gasto> gastoRequest) {

        List<Gasto> gastosSalvos = facade.cadastrarGastos(gastoRequest);
        return ResponseEntity.ok().body(gastosSalvos);
    }
}
