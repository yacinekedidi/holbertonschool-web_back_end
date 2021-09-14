import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const results = await Promise.all([uploadPhoto(), createUser()]);
    const [photo, user] = results;
    return ({
      photo,
      user,
    });
  } catch (err) {
    return ({
      photo: null,
      user: null,
    });
  }
}
