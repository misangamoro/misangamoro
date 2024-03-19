import './App.css';
import Compare from './lib/Soundcopare';
import { BrowserRouter, Routes, Route, Outlet } from 'react-router-dom';
import FolderComponent from './lib/inputFiles';
import ImageList from './lib/image';

function App() {
  return (
    <BrowserRouter>
      <Routes>
      <Route path="/">
        </Route>
        <Route index element={<FolderComponent />} />
        <Route path="2" element={<Compare />} />
        <Route path="3" element={<ImageList />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
