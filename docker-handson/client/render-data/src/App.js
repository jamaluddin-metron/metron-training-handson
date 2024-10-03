import './App.css';
import PaginatedTable from './view/data';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="/icons8-docker-logo-96.png" alt="logo" />
        <p>
          Docker HandsOn UI
        </p>
      </header>
      <div>
        <PaginatedTable />
      </div>
    </div>
  );
}

export default App;
