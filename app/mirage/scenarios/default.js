export default function(server) {
	server.createList('users', 5);
	server.loadFixtures();
}
