import React, { useState, useEffect } from 'react';
import Header from './Header';
import Footer from './Footer';
import CourseItem from './CourseItem';
import EnrollmentList from './EnrollmentList';

const CoursesPage = () => {

  const [courses, setCourses] = useState();
  const [enrolledCourses, setEnrolledCourses] = useState();

  useEffect(() => {
    fetch('http://127.0.0.1:5000/courses')
    .then(response => response.json())
    .then(data => { 
      if(data){
        setCourses(data);
      }
    })
    .catch(error => console.error('GET error:', error));
  }, []);

  useEffect(() => {
    let ID = localStorage.getItem('current_id'); //WIP GET STUDENT ID
    fetch('http://127.0.0.1:5000/student_courses/${ID}')
    .then(response => response.json())
    .then(data => { 
      if(data) {
        setEnrolledCourses(data);
      }
    })
    .catch(error => console.error('GET error:', error));
  }, []);

  function handleEnroll(event, course){
    event.preventDefault();

    let ID = localStorage.getItem('current_id'); //WIP GET STUDENT ID
    const postData = course;

    fetch('http://127.0.0.1:5000/enroll/${ID}', {method: 'POST', headers: {'Content-Type': 'application/json',}, body: JSON.stringify(postData), })
    .then(response => response.json())
    .then(data => {

    })
    .catch(error => console.error('POST error:', error));
}

  function handleRemove(event, courseID) {
    event.preventDefault();

    let ID = localStorage.getItem('current_id'); //WIP GET STUDENT ID
    const postData = courseID;

    fetch('http://127.0.0.1:5000/drop/${ID}', {method: 'POST', headers: {'Content-Type': 'application/json',}, body: JSON.stringify(postData), })
      .then(response => response.json())
      .then(data => {

    })
    .catch(error => console.error('POST error:', error));
  };

  return (
    <div style={{ 
      minHeight: '100vh', 
      display: 'flex', 
      flexDirection: 'column' 
    }}>
      <Header />
      
      <div style={{ 
        flex: 1,
        display: 'flex',
        padding: '20px',
        gap: '30px'
      }}>
        <div style={{ flex: 3 }}>
          <h2 style={{ color: '#004080' }}>Available Courses</h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
            gap: '20px'
          }}>
            {courses.map(course => (
              <CourseItem 
                key={course.id} 
                course={course} 
                onEnroll={(event) => handleEnroll(event, course)}
              />
            ))}
          </div>
        </div>
        
        <EnrollmentList 
          enrolledCourses={enrolledCourses}
          onRemove={(event) => handleRemove(event, courseID)}
        />
      </div>

      <Footer />
    </div>
  );
};

export default CoursesPage;
