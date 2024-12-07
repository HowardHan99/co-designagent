import miro_api

miro = miro_api.Miro(
  client_id='3458764607029223684',
  client_secret='fyvkvmdSpMLS4U5sYsUeWmkmvAfOVCJ9',
  redirect_url='http://localhost:3000/',
)

print(miro.auth_url)