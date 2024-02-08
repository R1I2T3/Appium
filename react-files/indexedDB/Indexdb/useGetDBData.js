import connect from "./connect";

const useGetDBData = () => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const getData = async (input) => {
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
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    return data;
  };
  return { getData };
};

export default useGetDBData;
