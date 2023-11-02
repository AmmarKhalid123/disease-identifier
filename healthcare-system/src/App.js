import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/header';
import Main from './components/main';

function App() {
  const [displays, setDisp] = useState(["block",  "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", "none", ]);
  const [showResult, setShowResult] = useState(false);
  if (showResult){
    return (
      <div style={{width: '100vw'}}>
        <Header />
        <h3 style={{margin: '50px', color: 'white'}}>Output</h3>
        <Main showResult={showResult} setShowResult={setShowResult} displays={displays} setDisp={setDisp} />
      </div>
    );
  }
  else{
    return (
      <div style={{width: '100vw'}}>
        <Header />
        <h3 style={{margin: '50px', color: 'white'}}>Page No. {displays.indexOf("block")+1}/ 13</h3>
        <Main showResult={showResult} setShowResult={setShowResult} displays={displays} setDisp={setDisp} />
      </div>
    );
  }
}

export default App;
