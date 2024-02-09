import connect from "./connect";
import { useCallback } from "react";
const useGetDBData = () => {
  const getDataFromDB = async (input) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const db = await connect();
    let data, index;
    const transaction = db.transaction("Profiling", "readonly");
    const objectStore = transaction.objectStore("Profiling");
    if (emailRegex.test(input)) {
      index = objectStore.index("email");
    } else {
      index = objectStore.index("phone_number");
    }
    const range = IDBKeyRange.only(input);
    try {
      const query = index.openCursor(range);
      const cursor = await new Promise((resolve, reject) => {
        query.onsuccess = () => resolve(query.result);
        query.onerror = reject;
      });
      if (cursor) {
        data = cursor.value;
        cursor.continue();
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    return data;
  };
  const getData = useCallback(getDataFromDB, []);
  return { getData };
};

export default useGetDBData;
