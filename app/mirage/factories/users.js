import Mirage, {faker} from 'ember-cli-mirage';

export default Mirage.Factory.extend({
	firstName: faker.name.firstName,
	lastName: faker.name.lastName,
	avatar: faker.image.avatar,
	username: faker.internet.userName,
	email: faker.internet.email,
	phone: faker.phone.phoneNumberFormat,
});