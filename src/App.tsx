import { useEffect, useState } from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ItemPage } from "./views/ItemPage";
import cars from "./data/cars.json";
import yachts from "./data/yachts.json";
import villas from "./data/villas.json";

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
          path='luxury-yachts'
          element={
            <ItemPage
              title='Miami &amp; Bahamas Yacht CHARTERS'
              media={{
                type: "image",
                link: "https://static.wixstatic.com/media/6da91d_7388e353a8b346168cd9a1e4f9e23afd~mv2.jpg/v1/fill/w_1504,h_399,fp_0.50_0.55,q_85,enc_auto/banner1_1593c2fb-08a8-4f9a-ae3d-c43a6ba987f5.jpg",
              }}
              data={yachts}
            />
          }
        />
        <Route
          path='luxury-villas'
          element={
            <ItemPage
              title='Miami Luxury Villa Rentals'
              media={{
                type: "image",
                link: "https://static.wixstatic.com/media/6da91d_4259bbab3c914d26bfed4c83b358c6fe~mv2.jpg/v1/fill/w_1885,h_500,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/6da91d_4259bbab3c914d26bfed4c83b358c6fe~mv2.jpg",
              }}
              data={villas}
            />
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
