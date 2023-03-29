package com.example.porquin.requests;

import com.fasterxml.jackson.annotation.JsonFormat;

import java.util.Date;

public class BuscarGastosRequest {

    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd-MM-yyyy")
    private Date inicioPeriodo;

    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd-MM-yyyy")
    private Date fimPeriodo;

    public Date getInicioPeriodo() {
        return inicioPeriodo;
    }

    public void setInicioPeriodo(Date inicioPeriodo) {
        this.inicioPeriodo = inicioPeriodo;
    }

    public Date getFimPeriodo() {
        return fimPeriodo;
    }

    public void setFimPeriodo(Date fimPeriodo) {
        this.fimPeriodo = fimPeriodo;
    }
}
