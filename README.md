# 📊 Dashboard de Operações: Gestão de Equipes em Campo

## 🎯 O Problema de Negócio
A coordenação de equipes de campo (instalações e visitas técnicas) exige monitoramento em tempo real para evitar ociosidade e garantir o cumprimento dos Acordos de Nível de Serviço (SLA). Sem visibilidade centralizada, os gestores têm dificuldade em identificar quais equipes apresentam gargalos, quais regiões concentram mais atrasos e qual o tempo médio real gasto em cada tipo de serviço.

## 💡 A Solução
Este projeto consiste em um painel gerencial interativo desenvolvido em Power BI. Ele consolida os dados de agendamentos e execuções diárias, transformando-os em indicadores operacionais claros. O dashboard permite que a liderança monitore a performance das equipes, audite a taxa de conclusão no prazo e tome decisões baseadas em dados para equilibrar a capacidade de atendimento.

## ⚙️ Indicadores (KPIs) Analisados
* **Volume Operacional:** Total de Ordens de Serviço (OS) ativas.
* **Carga de Trabalho:** Total de horas de execução em campo.
* **Eficiência (SLA):** Taxa percentual de entregas realizadas rigorosamente dentro do prazo.
* **Performance:** Tempo médio de atendimento por serviço e por equipe.

## 📸 Visão Geral do Painel
![Dashboard de Operações](dashboard_print.png)

## 🛠️ Tecnologias e Técnicas Utilizadas
* **Python (Pandas):** Geração e modelagem estruturada da base de dados simulada.
* **Power Query (ETL):** Limpeza, tipagem e adequação de localidade dos dados brutos (conversão de padrões numéricos).
* **Power BI (DAX):** Criação de medidas personalizadas (SLA, Tempo Médio) e modelagem de visualização de dados focada em UX/UI corporativa.

---
*Projeto focado em inteligência operacional e otimização de recursos logísticos.*
