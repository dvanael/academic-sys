
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  cpf VARCHAR(14) UNIQUE NOT NULL,
  admission_date DATE NOT NULL DEFAULT CURRENT_DATE,
);


CREATE TABLE courses (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  total_hours INT NOT NULL,
  enrollment_fee NUMERIC(10,2) NOT NULL,
  status BOOLEAN NOT NULL DEFAULT FALSE,
);


CREATE TABLE enrollments (
  id SERIAL PRIMARY KEY,
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
  status BOOLEAN NOT NULL DEFAULT FALSE,

  CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES students (id) ON DELETE CASCADE,

  CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE,

  CONSTRAINT unique_student_course UNIQUE (student_id, course_id),
);
