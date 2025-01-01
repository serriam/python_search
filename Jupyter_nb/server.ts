import fs from 'fs';

type User = {
    firstName: string;   
};

fetch('https://dummyjson.com/users?limit=0')
.then(res => {
    if (!res.ok){
        throw new Error(`HTTP error! status, no network`);
    }
        return res.json()})
.then(data=>{
    const firstNames = data.users.map((user: any) => user.firstName);
    console.log(firstNames);

    const outputData = {
        firstNames: firstNames
    };
    fs.writeFileSync('dummy.json', JSON.stringify(outputData, null, 2));
    console.log('Data saved to dummy.json');
})

.catch(err => {
    console.error('error fetching data:', err);
});