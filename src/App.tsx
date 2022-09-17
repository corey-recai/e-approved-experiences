import { useEffect, useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ExoticCars } from "./views/ExoticCars";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<ExoticCars />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
