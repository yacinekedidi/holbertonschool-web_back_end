import { createUser, uploadPhoto } from './utils';

function handleProfileSignup() {
  Promise.all([createUser(), uploadPhoto()]).then((data) => {
    const [{ firstName, lastName }, { body }] = data;
    console.log(`${body} ${firstName} ${lastName}`);
  }).catch(() => console.log('Signup system offline'));
}

export default handleProfileSignup;
