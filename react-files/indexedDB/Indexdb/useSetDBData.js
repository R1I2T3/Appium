import { useCallback } from "react";
import connect from "./connect";

const useSetDBData = () => {
  const setDataIntoDB = async (data) => {
    const db = await connect();
    if (db) {
      const transaction = db.transaction("Profiling", "readwrite");
      const action = transaction.objectStore("Profiling");
      action.add(data);
    }
  };
  const setData = useCallback(setDataIntoDB, []);
  return { setData };
};

export default useSetDBData;
