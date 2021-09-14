import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName),
    uploadPhoto(fileName)]).then((data) => data.map((result) => (result.status === 'fullfilled' ? ({ status: result.status, value: result.value }) : ({ status: result.status, value: result.reason }))));
}
