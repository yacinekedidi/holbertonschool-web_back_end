function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    resolve({ firstName, lastName }).catch(() => reject());
  });
}

export default signUpUser;
