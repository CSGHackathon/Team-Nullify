export default function(server) {
	server.createList('users', 1);
	server.loadFixtures();
}
