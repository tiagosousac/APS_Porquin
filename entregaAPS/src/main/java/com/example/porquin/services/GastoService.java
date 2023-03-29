package com.example.porquin.services;

import com.example.porquin.dao.Categoria;
import com.example.porquin.dao.Gasto;
import com.example.porquin.repository.GastoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
@Scope("singleton")
public class GastoService {
    @Autowired
    GastoRepository gastoRepository;
    public Gasto cadastrarGasto(Gasto gasto){
        return gastoRepository.save(gasto);
    }

    public List<Gasto> buscarGastos(Date inicioPeriodo, Date fimPeriodo){
        return gastoRepository.findGastoByInitialDateBetween(inicioPeriodo, fimPeriodo);
    }

    public List<Gasto> cadastrarGastos(List<Gasto> gastos){
        List<Gasto> gastosSalvos = new ArrayList<Gasto>();
        for(Gasto gasto : gastos){
            gastosSalvos.add(gastoRepository.save(gasto));
        }
        return gastos;
    }
}
