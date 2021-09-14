import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((data) => {
      const arr = data.map((result) => (result.status === 'rejected'
        ? ({ ...result, value: result.reason })
        : result
      ));
      return arr;
    });
}
