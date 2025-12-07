
# 📘 Academic System

---

## Funcionalidades

Este projeto implementa gerenciamento de **Alunos**, **Cursos**, **Matrículas**, **Financeiro**, **Relatórios HTML**, **API REST**, **SQL**, e **Docker**.

---

## **Como Rodar**

### Pré-requisitos

* Docker
* Docker Compose

Execute:

```bash
docker-compose up --build
```

Após iniciar:

* Interface:
  [http://localhost:8000](http://localhost:8000)

* API:
  [http://localhost:8000/api/](http://localhost:8000/api/)

---

## 🔗 **API Endpoints**

### 📘 **Students**

| Método    | Endpoint          | Descrição      |
| --------- | ----------------- | -------------- |
| GET       | `/students/`      | Lista todos    |
| POST      | `/students/`      | Cria aluno     |
| GET       | `/students/<id>/` | Detalha aluno  |
| PUT/PATCH | `/students/<id>/` | Atualiza aluno |
| DELETE    | `/students/<id>/` | Remove aluno   |

---

### 📘 **Courses**

| Método    | Endpoint         | Descrição      |
| --------- | ---------------- | -------------- |
| GET       | `/courses/`      | Lista todos    |
| POST      | `/courses/`      | Cria aluno     |
| GET       | `/courses/<id>/` | Detalha aluno  |
| PUT/PATCH | `/courses/<id>/` | Atualiza aluno |
| DELETE    | `/courses/<id>/` | Remove aluno   |

---

### 📘 **Enrollments**

Esses endpoints **não** usam router (como você implementou).

| Método | Endpoint                      | Descrição                     |
| ------ | ----------------------------- | ----------------------------- |
| POST   | `/enrollments/create/`        | Criar matrícula               |
| POST   | `/enrollments/<id>/pay/`      | Marcar como paga              |
| GET    | `/students/<id>/enrollments/` | Listar matrículas de um aluno |

---

### 📘 **Reports**

| Método | Endpoint                          | Descrição                     |
| ------ | --------------------------------- | ----------------------------- |
| GET    | `/report/enrollments-per-course/` | Total de matrículas por curso |


---

## **Tecnologias Utilizadas**

* Python 3
* Django 5
* Django Rest Framework (DRF)
* PostgreSQL
* Docker + Docker Compose
* HTML + Django Templates

---