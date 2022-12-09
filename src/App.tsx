import { useEffect, useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ItemPage } from "./views/ItemPage";
import cars from "./data/cars.json";
import yachts from "./data/yachts.json";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path='/'
          element={
            <ItemPage
              title='Miami Exotic Car Rentals'
              media={{
                type: "video",
                link: "https://video.wixstatic.com/video/6da91d_1cf23ceb66ae4b758c05b25b290d5a52/1080p/mp4/file.mp4",
              }}
              data={cars}
            />
          }
        />
        <Route
          path='/luxury-yachts'
          element={
            <ItemPage
              title='MIAMI &amp; BAHAMAS YACHT CHARTERS'
              media={{
                type: "image",
                link: "https://static.wixstatic.com/media/6da91d_7388e353a8b346168cd9a1e4f9e23afd~mv2.jpg/v1/fill/w_1504,h_399,fp_0.50_0.55,q_85,enc_auto/banner1_1593c2fb-08a8-4f9a-ae3d-c43a6ba987f5.jpg",
              }}
              data={yachts}
            />
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
