package com.example.porquin.services;

import com.example.porquin.dao.Categoria;
import com.example.porquin.dao.Gasto;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.List;
@Service
public class Facade {
    @Autowired
    private GastoService gastoService;

    @Autowired
    private CategoriaService categoriaService;

    public Gasto cadastrarGasto(Gasto gasto){
        return gastoService.cadastrarGasto(gasto);
    }
    public List<Gasto> buscarGastos(Date inicioPeriodo, Date fimPeriodo){
        return gastoService.buscarGastos(inicioPeriodo, fimPeriodo);
    }

    public Categoria cadastrarCategoria(Categoria categoria){
        return categoriaService.cadastrarCategoria(categoria);
    }

    public List<Gasto> cadastrarGastos(List<Gasto> gastos){
        return gastoService.cadastrarGastos(gastos);
    }
}
