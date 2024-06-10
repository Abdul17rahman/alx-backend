import { createClient, print } from 'redis';
import util from "node:util"

const client = createClient();
client.get = util.promisify(client.get)

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

try {
  client.connected;
  console.log('Redis client connected to the server');
} catch (err) {
  console.log(`Redis client not connected to the server: ${err}`);
}

const setNewSchool =async (schoolName, value) => {
  await client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const data = await client.get(schoolName)
  console.log(data)
};

(async () => {
  
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})()
