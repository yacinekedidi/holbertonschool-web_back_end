import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((data) => {
      const arr = data.map((result) => {
        const { status } = result;
        if (status === 'rejected') return ({ status, value: result.reason });
        return result;
      });
      return arr;
    });
}
