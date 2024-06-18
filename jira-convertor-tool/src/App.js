// import React, { useState } from 'react';
import './App.css';
import backgroundImage from './dark-grunge-texture.jpg';
import '@trimbleinc/modus-react-bootstrap/css/dist/modus-react-bootstrap.min.css';

import {Button} from '@trimbleinc/modus-react-bootstrap';
import {Form} from '@trimbleinc/modus-react-bootstrap';

function App() {


  return (
    <div className="App" style={{backgroundImage: 
      `url(${backgroundImage})`, height: '100vh', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
      <div style={{background: 'rgba(255, 255, 255, 0.6)', padding: '20px', margin: '40px', width: '80%'}}>
        <h1>Provide us with details about your requirements.</h1>
        <div>
    <br></br>
    <Form>
    <div key="custom-inline-checkbox">
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox"
      label="UI"
      className="mr-3"
    />
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox"
      label="API/Services"
      checked
      className="mr-3"
    />
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox"
      label="DB"
      className="mr-3"
    />
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox"
      label="Mobile"
      className="mr-3"
    />
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox"
      label="All"
      className="mr-3"
    />
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox"
      label="None"
      className="mr-3"
    />
  </div>
  <Form.Group controlId="formBasicEmail">
    <Form.Label>Team Structure</Form.Label>
    <Form.Control as="input" placeholder="Placeholder Text"></Form.Control>
  </Form.Group>
  <Form.Group controlId="formBasicEmail1">
    <Form.Label>Architectural Implications</Form.Label>
    <Form.Control as="input" placeholder="Placeholder Text"></Form.Control>
  </Form.Group>
  <Form.Group controlId="formBasicEmail">
    <Form.Label>Industry</Form.Label>
    <Form.Control as="input" placeholder="Placeholder Text"></Form.Control>
  </Form.Group>
  <div key="custom-inline-checkbox">
    <Form.Check
      custom
      inline
      type="checkbox"
      id="custom-inline-checkbox-1"
      label="Does it require a cloud solution"
      className="mr-3"
    />
  </div>
  <Form.Group controlId="exampleForm.ControlTextarea1">
    <Form.Label className="label-lg">Describe the Requirements in detail</Form.Label>
    <Form.Control as="textarea" rows={5} size="lg">
    </Form.Control>
  </Form.Group>
  <Button variant="primary" type="submit">
    Submit
  </Button>
</Form>
</div>
      </div>

    </div>
  );
}

export default App;