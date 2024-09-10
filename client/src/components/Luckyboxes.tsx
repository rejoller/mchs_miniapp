import { useState } from "react";
import firetree from "../assets/fire.png";
import { userProps } from "../interfaces/user";
import { useEffect, useState } from "react";

function Luckyboxes(props: userProps) {
  const [box, setBox] = useState(false)
  const [isClicked, setIsClicked] = useState(false)


  return (
    <div className=" flex justify-center items-center h-screen">
      <div className="text-center">
        <button onClick={() => setButton(button + 1)}>{button}</button>
        <img src={firetree} alt="gift" width={256} />
      </div>
    </div>
  );
}

export default Luckyboxes;
