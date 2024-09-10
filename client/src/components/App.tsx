import Luckyboxes from "./Luckyboxes";
import { TG, request } from "../api/requests";
import { useEffect, useState } from "react";


function App() {
  const [user, setUser] = useState({
    id: 0,
    username: "Unknown",
    Luckyboxes: 0,
    balance: 0

  })


  useEffect(() => {
    async function fetchData() {
      const response = await request("user");
      setUser(response)
    }
  }, [] ) 

  return (
    <>
      <Luckyboxes data= {user} setUser={setUser} />
    </>
  );
}

export default App;
