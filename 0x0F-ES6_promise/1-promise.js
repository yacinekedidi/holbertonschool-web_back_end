const getFullResponseFromAPI = (success) =>
  // eslint-disable-next-line implicit-arrow-linebreak
  new Promise((resolve, reject) => {
    if (success) resolve({ status: 200, body: 'Success' });
    // eslint-disable-next-line prefer-promise-reject-errors
    else reject({ error: 'The fake API is not working currently' });
  });

export default getFullResponseFromAPI;
