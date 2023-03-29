package com.example.porquin.controller;

import com.example.porquin.dao.Gasto;
import com.example.porquin.repository.GastoRepository;
import com.example.porquin.requests.BuscarGastosRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController()
public class BancoAPI {

    @Autowired
    GastoRepository gastoRepository;
    @PostMapping("/buscar-gastos")
    public ResponseEntity<List<Gasto>> buscarGastos(@RequestBody BuscarGastosRequest buscarGastosRequest){
        List<Gasto> gastos = new ArrayList<Gasto>();
        gastos = gastoRepository.findGastoByInitialDateBetween(buscarGastosRequest.getInicioPeriodo(), buscarGastosRequest.getFimPeriodo());

        return ResponseEntity.ok(gastos);
    }
}
