const connect = () => {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open("Trinetra");
    request.onerror = (event) => {
      console.log("Error while connecting db");
      reject(event.target.error);
    };
    let db;
    if (!db) {
      request.onupgradeneeded = async (event) => {
        const db = await event.target.result;
        const objectStore = db.createObjectStore("Profiling", {
          autoIncrement: true,
        });
        objectStore.createIndex("email", "email", { unique: true });
        objectStore.createIndex("phone_number", "phone_number", {
          unique: true,
        });
      };
    }
    request.onsuccess = () => {
      db = request.result;
      resolve(db);
    };
  });
};

export default connect;
