package com.example.porquin.dao;

import com.fasterxml.jackson.annotation.JsonFormat;
import jakarta.persistence.*;
import java.util.Date;

@Entity
public class Gasto {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    private long id;

    @Column(name = "nome")
    private String nome;

    @Override
    public String toString() {
        return "Gasto{" +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", valor=" + valor +
                ", categoria='" + categoria + '\'' +
                '}';
    }

    @Column(name = "valor")
    private long valor;

    public Date getDataOcorrida() {
        return dataOcorrida;
    }

    public void setDataOcorrida(Date dataOcorrida) {
        this.dataOcorrida = dataOcorrida;
    }

    @Column(name = "dataOcorrida")
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd-MM-yyyy")
    private Date dataOcorrida;

    @ManyToOne(cascade = {CascadeType.ALL})
    private Categoria categoria;

    public Gasto(long id, String nome, long valor, Categoria categoria) {
        this.id = id;
        this.nome = nome;
        this.valor = valor;
        this.categoria = categoria;
    }

    public Gasto() {
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public long getValor() {
        return valor;
    }

    public void setValor(long valor) {
        this.valor = valor;
    }

    public Categoria getCategoria() {
        return categoria;
    }

    public void setCategoria(Categoria categoria) {
        this.categoria = categoria;
    }
}
