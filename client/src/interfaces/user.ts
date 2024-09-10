import { useState } from "react";
export interface IUser {
  id: number;
  username: string;
  Luckyboxes: number;
  balance: number;
}

export interface userProps {
  data: IUser;
  setUser: (user: IUser) => void;
}
