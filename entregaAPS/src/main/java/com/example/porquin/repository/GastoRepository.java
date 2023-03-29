package com.example.porquin.repository;

import com.example.porquin.dao.Gasto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.Date;
import java.util.List;

@Repository
public interface GastoRepository extends JpaRepository<Gasto, Long> {
    Gasto save(Gasto gasto);

    @Query("SELECT g FROM Gasto g WHERE g.dataOcorrida BETWEEN :dateInitial and :dateFinal")
    List<Gasto> findGastoByInitialDateBetween(
            @Param("dateInitial") Date dataInicial,
            @Param("dateFinal") Date dateFinal);
}
